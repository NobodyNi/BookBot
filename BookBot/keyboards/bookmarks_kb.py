from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from BookBot.lexicon.lexicon import LEXICON
from BookBot.services.file_handling import book


def create_bookmarks_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for i in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{i} - {book[i][:100]}',
            callback_data=str(i)
        ))

    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['edit_bookmarks_button'],
            callback_data='edit_bookmarks'
        ),
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        ),
        width=2
    )
    return kb_builder.as_markup()


def create_edit_keyboard(*args: int) -> InlineKeyboardMarkup:
    kb_builder = InlineKeyboardBuilder()

    for i in sorted(args):
        kb_builder.row(InlineKeyboardButton(
            text=f'{LEXICON['del']} {i} - {book[i][:100]}',
            callback_data=f'{i}del'
        ))

    kb_builder.row(
        InlineKeyboardButton(
            text=LEXICON['cancel'],
            callback_data='cancel'
        )
    )
    return kb_builder.as_markup()

